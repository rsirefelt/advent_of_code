#include <iostream>
#include <vector>


int main() {
    // Values taken from python output
    const std::vector<uint> diff =
    {
        0,  17, 23,  36, 37, 42, 54,  64, 83
    };

    const std::vector<uint> bus_id =
    {
        23, 37, 431, 13, 17, 19, 409, 41, 29
    };
    std::cout << diff[1] << "\n";

    const uint max_id = 431U;
    const uint max_id_diff = 23U;

    unsigned long long int t = (100000000000000 / max_id) * max_id - max_id_diff;

    bool all_true;
    while(true)
    {
        all_true = true;
        for(uint i=0U; i < diff.size(); ++i)
        {
            if ( ((t + diff[i]) % bus_id[i]) != 0)
            {
                all_true = false;
                break;
            }
        }
        if(all_true)
        {
            std::cout << Searched timestamp << "\n";
            break;
        }
        else
        {
            t += max_id;
            if(t % 100000000000 < max_id)
            {
                std::cout << t << "\n";
            }
        }

    }
    return 0;
}