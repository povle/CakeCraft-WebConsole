#include "api.h"

namespace AJ{
    struct sysinfo API::Stats::mem_info{};
    struct statvfs API::Stats::buffer{};
    unsigned long long API::Stats::last_total_user;
    unsigned long long API::Stats::last_total_user_low;
    unsigned long long API::Stats::last_total_sys;
    unsigned long long API::Stats::last_total_idle;

    char const* API::greet(){
       return "Hello, world!";
    }
    API::Stats::Stats(){
        FILE* file = fopen("/proc/stat", "r");
        fscanf(file, "cpu %llu %llu %llu %llu", &last_total_user, &last_total_user_low, &last_total_sys, &last_total_idle);
        fclose(file);
    }

    float API::Stats::get_ram_usage(){
        int err = sysinfo (&mem_info);
        float result;
        if(!err){
            result = (float)(mem_info.totalram - mem_info.freeram) / (float)mem_info.totalram * (float)100;
        }else{
            result = -1;
        }
        std::cout << "totalram\toccupied\tfree\tshared\t\tbuf/temp\n";
        std::cout << mem_info.totalram / 1024 / 1024 << "\t\t";
        std::cout << (mem_info.totalram - mem_info.freeram) / 1024 / 1024 << "\t\t";
        std::cout << mem_info.freeram / 1024 / 1024 << "\t";
        std::cout << mem_info.sharedram / 1024 / 1024 << "\t\t";
        std::cout << mem_info.bufferram / 1024 / 1024 << "\t\t";
        std::system("free -m");
        return result;
    }
    float API::Stats::get_cpu_usage(){
        unsigned long long total_user, total_user_low, total_sys, total_idle;
        FILE* file = fopen("/proc/stat", "r");
        fscanf(file, "cpu %llu %llu %llu %llu", &total_user, &total_user_low, &total_sys, &total_idle);
        int err = fclose(file);
        float result;
        if(!err){
            if(total_user < last_total_user || total_user_low < last_total_user_low || total_sys < last_total_sys || total_idle < last_total_idle){
                result = -2;
            }else{
                unsigned long long temp = (total_user - last_total_user_low) + (total_user_low - last_total_user_low) + (total_sys - last_total_sys);
                result = (long double)temp / (long double)(temp + (total_idle - last_total_idle)) * (long double)100;
            }
        }else{
            result = -1;
        }

        last_total_user = total_user;
        last_total_user_low = total_user_low;
        last_total_sys = total_sys;
        last_total_idle = total_idle;

        return result;
    }
    float API::Stats::get_disk_usage(){
        int err = statvfs("/", &buffer);
        float result;
        if (!err) {
            result = ((float)(buffer.f_blocks - buffer.f_bfree) / (float)buffer.f_blocks) * (float)100;
        }else{
            result = -1;
        }
        return result;
    }
    char const* API::RCON::exec_command(std::string cmd){
        return "1234";
    }
    char const* API::RCON::get_history(int count, int offset){
        return "1234";
    }
    char const* API::BackupManagement::make(std::string name, std::string desc){
        return "1234";
    }
    char const* API::BackupManagement::info(int type, std::string name_or_timestamp){
        return "1234";
    }
    char const* API::BackupManagement::list(int count, int type_from, std::string from, int type_to, std::string to){
        return "1234";
    }
    char const* API::BackupManagement::switch_to(int type, std::string name_or_timestamp){
        return "1234";
    }

}
