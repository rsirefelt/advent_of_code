#pragma once
/*
Christmas Template Library
*/

#include <algorithm>
#include <fstream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>

// Return the keys of the map as a vector
template<typename T1, typename T2>
std::vector<T1> map_keys(const std::map<T1, T2>& m) {
    std::vector<T1> keys;
    keys.reserve(m.size());
    for(const auto& kv : m) {
        keys.push_back(kv.first);
    }
    return keys;
}

template<typename K, typename V>
std::map<K, V> make_map(const std::vector<std::pair<K, V>>& vec) {
    return std::map<K, V>(vec.begin(), vec.end());
}

template<typename T>
std::pair<T, T> make_pair(const std::vector<T>& vec) {
    return std::make_pair(vec[0], vec[1]);
}

template<typename T, typename Tout = typename T::iterator::value_type>
std::set<Tout> make_set(const T& vec) {
    return std::set<Tout>(vec.begin(), vec.end());
}

// Return true if b is a subset of a
template<typename T>
bool is_subset(const std::set<T>& a, const std::set<T>& b) {
    return std::includes(a.begin(), a.end(), b.begin(), b.end());
}

// Return true if b is a subset of a
template<typename T>
bool is_subset(const std::vector<T>& a, const std::set<T>& b) {
    std::set<T> a_s(a.begin(), a.end());
    return is_subset(a_s, b);
}

template<typename T>
bool in(const T& t, const std::set<T>& s) {
    return s.find(t) != s.end();
}

template<typename Tvec, typename T = typename Tvec::value_type::value_type>
std::set<T> set_union(const Tvec& sets) {
    std::set<T> retval;
    for (const auto& vec: sets) {
        retval.insert(vec.begin(), vec.end());
    }
    return retval;
}

template<typename T>
std::set<T> intersection(const std::vector<std::set<T>>& sets) {
    std::set<T> retval;
    if (sets.size() > 0) {
        retval.insert(sets[0].begin(), sets[0].end());
        for (auto& s: sets) {
            std::set<T> new_set;
            std::set_intersection(
                s.begin(), s.end(),
                retval.begin(), retval.end(),
                std::inserter(new_set, new_set.begin()));
            retval = std::move(new_set);
        }
    }
    return retval;
}

// Return true if v is in range [min_v, max_v]
bool in_range(int min_v, int v, int max_v) {
    return min_v <= v && v <= max_v;
}

// Return true if str ends with needle
bool ends_with(const std::string& str, const std::string& needle) {
    if (needle.size() < str.size()) {
        return std::equal(needle.rbegin(), needle.rend(), str.rbegin());
    }
    return false;
}

std::string slice(const std::string& str, size_t start, int len = 0) {
    size_t slen;
    if (len > 0) {
        slen = len;
    } else if (len == 0) {
        slen = std::string::npos;
    } else {
        slen = str.length() + len;
    }
    return str.substr(start, slen);
}

bool is_hex(char c) {
    return (c >= '0' && c <= '9') || (c >= 'a' && c <= 'f');
}

std::string read_file(const std::string& filename) {
    std::ifstream ifs(filename);
    if (ifs.fail()) {
        throw std::runtime_error("Could not open file");
    }

    std::string str;
    ifs.seekg(0, std::ios::end);   
    str.reserve(ifs.tellg());
    ifs.seekg(0, std::ios::beg);

    str.assign((std::istreambuf_iterator<char>(ifs)),
                std::istreambuf_iterator<char>());
    return str;
}

std::vector<std::string> split(const std::string& str, const std::string& delim) {
    std::vector<std::string> strvec;
    size_t pos = 0;
    int n_str = str.size();
    while(pos < n_str) {
        size_t end_pos = str.find(delim, pos);
        if (end_pos == std::string::npos) {
            strvec.push_back(str.substr(pos));
            break;
        }
        if (end_pos > pos) {
            strvec.push_back(str.substr(pos, end_pos - pos));
        }
        pos = end_pos + delim.length();
    };
    return strvec;
}

std::string replace(const std::string& str, char before, char after) {
    std::string retval = str;
    std::replace(retval.begin(), retval.end(), before, after);
    return retval;
}

std::string strip(const std::string& str) {
    std::string whites(" \t\f\v\n\r");
    std::size_t l = str.find_first_not_of(whites);
    std::size_t r = str.find_last_not_of(whites);
    if (r != std::string::npos) {
        return str.substr(l, r - l + 1);
    } else {
        return "";
    }
}

long stol(const std::string& s) {
    return std::stol(s);
}

template<typename Tvecin,
    typename F,
    typename T = typename Tvecin::iterator::value_type,
    typename Tout = typename std::result_of<F(T)>::type>
std::vector<Tout> map(F func, const Tvecin& values) {
    std::vector<Tout> retval;
    retval.reserve(values.size());
    for (const auto& value: values) {
        retval.push_back(func(value));
    }
    return retval;
}

template<typename T, typename F>
std::vector<T> filter(const std::vector<T>& vec, F pred) {
    std::vector<T> retval;
    std::copy_if(vec.begin(), vec.end(), std::back_inserter(retval), pred);
    return retval;
}

template<typename T>
std::vector<T> slice(const std::vector<T>& vec, size_t start, size_t end = 0) {
    if (end == 0) end = vec.size();
    return std::vector<T>(vec.begin() + start, vec.begin() + end);
}

template<typename T>
T max(const std::vector<T>& vec) {
    return *std::max_element(vec.begin(), vec.end());
}

template<typename T>
T min(const std::vector<T>& vec) {
    return *std::min_element(vec.begin(), vec.end());
}

template<typename T>
T sum(const std::vector<T>& vec) {
    return std::accumulate(vec.begin(), vec.end(), T(0));
}

template<typename T>
T prod(const std::vector<T>& vec) {
    return std::accumulate(vec.begin(), vec.end(), T(1), std::multiplies<>());
}

template<typename T>
void sort(std::vector<T>& vec) {
    std::sort(vec.begin(), vec.end());
}

template<typename T>
std::vector<T> sorted(const std::vector<T>& vec) {
    auto retval = vec;
    std::sort(retval.begin(), retval.end());
    return retval;
}

template<typename Tvec, typename T = typename Tvec::value_type>
size_t count(const Tvec& vec, const T& value) {
    return std::count(vec.begin(), vec.end(), value);
}

int gcd(int a, int b) { 
    if (b == 0) 
        return a; 
    return gcd(b, a % b); 
} 
  
int lcm(const std::vector<int>& vec) { 
    int ans = vec[0]; 
    for (int i = 1; i < vec.size(); i++) {
        ans = vec[i] * ans / gcd(vec[i], ans); 
    }
      return ans; 
}

void setbit(int64_t& value, int bit) {
    value |= (1LL << (35-bit));
}

void clearbit(int64_t& value, int bit) {
    value &= ~(1LL << (35-bit));
}
