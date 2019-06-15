#include "api.h"

namespace AJ{
    char const* API::greet(){
       return "hello, world";
    }
    float API::Stats::get_ram_usage(){
        return 99.9;
    }
    float API::Stats::get_cpu_usage(){
        return 99.9;
    }
    float API::Stats::get_disk_usage(){
        return 99.9;
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
