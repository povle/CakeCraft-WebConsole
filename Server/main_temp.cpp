#include <sys/types.h>
#include <sys/sysinfo.h>
#include <iostream>
#include <cstdint>
#include <cstdlib>
#include <cstdio>

struct sysinfo memInfo;

static unsigned long long lastTotalUser, lastTotalUserLow, lastTotalSys, lastTotalIdle;

void init(){
    FILE* file = fopen("/proc/stat", "r");
    fscanf(file, "cpu %llu %llu %llu %llu", &lastTotalUser, &lastTotalUserLow,
        &lastTotalSys, &lastTotalIdle);
    fclose(file);
}

double getCurrentValue(){
    double percent;
    FILE* file;
    unsigned long long totalUser, totalUserLow, totalSys, totalIdle, total;

    file = fopen("/proc/stat", "r");
    fscanf(file, "cpu %llu %llu %llu %llu", &totalUser, &totalUserLow,
        &totalSys, &totalIdle);
    fclose(file);

    if (totalUser < lastTotalUser || totalUserLow < lastTotalUserLow ||
        totalSys < lastTotalSys || totalIdle < lastTotalIdle){
        //Overflow detection. Just skip this value.
        percent = -1.0;
    }
    else{
        total = (totalUser - lastTotalUser) + (totalUserLow - lastTotalUserLow) +
            (totalSys - lastTotalSys);
        percent = total;
        total += (totalIdle - lastTotalIdle);
        percent /= total;
        percent *= 100;
    }

    lastTotalUser = totalUser;
    lastTotalUserLow = totalUserLow;
    lastTotalSys = totalSys;
    lastTotalIdle = totalIdle;

    return percent;
}

int main(){
        sysinfo (&memInfo);
        float RAM_usage = (double)((memInfo.totalram - memInfo.freeram) * memInfo.mem_unit) / (double)(memInfo.totalram * memInfo.mem_unit);
        float usage2 = (double)((memInfo.totalram - memInfo.freeram + memInfo.totalswap - memInfo.freeswap)*memInfo.mem_unit) / (double)((memInfo.totalram + memInfo.totalswap) * memInfo.mem_unit);
        std::cout << "RAM usage is " << RAM_usage*100 << "%\n";
        std::cout << "usage2 is " << usage2*100 << "%\n";
        std::cout << "It's working!\n";
        return 0;
}
