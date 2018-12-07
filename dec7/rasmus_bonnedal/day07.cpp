#include <fstream>
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <unordered_set>
#include <vector>

class Task {
public:
    Task(char name) : 
        _name(name)
        , _inProgress(false)
        , _workLeft(60 +  _name - 'A' + 1) {
    }

    void addDep(char dep) {
        _deps.insert(dep);
    }

    void removeDep(char dep) {
        _deps.erase(dep);
    }

    char getName() const {
        return _name;
    }

    bool isInProgress() const {
        return _inProgress;
    }

    void setWorkLeft(int t) {
        _workLeft = t;
    }

    bool doWork() {
        if (_inProgress && --_workLeft == 0) {
            _inProgress = false;
            return true;
        }
        return false;
    }

    bool tryAssign() {
        if (_deps.empty() && !_inProgress && _workLeft > 0) {
            _inProgress = true;
            return true;
        } else {
            return false;
        }
    }

private:
    const char _name;
    std::unordered_set<char> _deps;
    bool _inProgress;
    int _workLeft;
};

using TaskMap = std::map<char, std::unique_ptr<Task>>;

class Worker {
public:
    Worker() : _workItem(0) {}

    bool hasWork() const {
        return _workItem != 0;
    }

    char getWork() const {
        return _workItem;
    }

    void setWork(char work) {
        _workItem = work;
    }

private:
    char _workItem;
};

using WorkerVec = std::vector<Worker>;

Task& getOrCreate(TaskMap& tasks, char c) {
    auto it = tasks.find(c);
    if (it != tasks.end()) {
        return *it->second;
    } else {
        return *tasks.insert(std::make_pair(c, std::make_unique<Task>(c))).first->second;
    }
}

void addTask(TaskMap& tasks, char a, char b) {
    Task& t = getOrCreate(tasks, b);
    getOrCreate(tasks, a);
    t.addDep(a);
}

TaskMap parseTasks(std::istream& input) {
    TaskMap tasks;
    std::string s;
    while (std::getline(input, s)) {
        addTask(tasks, s[5], s[36]);
    }
    return tasks;    
}

std::string doWork(TaskMap& tasks, WorkerVec& workers) {
    std::string result;
    for (auto& kv : tasks) {
        Task& t = *kv.second;
        if (t.doWork()) {
            result += t.getName();
            for (auto& kv : tasks) {
                kv.second->removeDep(t.getName());
            }
        }
    }
    for (auto& w : workers) {
        if (w.hasWork() && !tasks[w.getWork()]->isInProgress()) {
            w.setWork(0);
        }
    }
    for (auto c : result) {
        tasks.erase(c);
    }
    return result;
}

void assignWork(TaskMap& tasks, WorkerVec& workers) {
    for (auto& w: workers) {
        if (!w.hasWork()) {
            for (auto& kv : tasks) {
                Task& t = *kv.second;
                if (t.tryAssign()) {
                    w.setWork(t.getName());
                    break;
                }
            }
        }
    }
}

int runner(TaskMap& tasks, int nWorkers, std::string& result) {
    WorkerVec workers(nWorkers);
    int second = 0;
    while (!tasks.empty()) {
        assignWork(tasks, workers);
        result += doWork(tasks, workers);
        second++;
    }
    return second;
}

std::string problemA(std::istream& input) {
    TaskMap tasks = parseTasks(input);
    for (auto& kv : tasks) {
        kv.second->setWorkLeft(1);
    }

    std::string result;
    runner(tasks, 1, result);
    return result;
}

int problemB(std::istream& input) {
    TaskMap tasks = parseTasks(input);
    std::string result;
    return runner(tasks, 5, result);
}

int main(int, char**) {
    std::ifstream input("../input_07.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }

    std::cout << problemA(input) << std::endl;
    input.clear();
    input.seekg(0);
    std::cout << problemB(input) << std::endl;

    return 0;
}
