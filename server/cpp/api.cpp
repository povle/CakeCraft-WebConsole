#include "api.h"

namespace AJ{
    struct sysinfo API::Stats::mem_info{};
    struct statvfs API::Stats::buffer{};
    unsigned long long API::Stats::ram_total;
    unsigned long long API::Stats::ram_free;
    unsigned long long API::Stats::ram_available;

    char const* API::greet(){
       return "Hello, world!";
    }
    API::Stats::Stats(){

    }

    std::vector<unsigned long long> API::Stats::get_cpu_data(){
        std::vector<unsigned long long> data(10, 0);
        FILE* file = fopen("/proc/stat", "r");
        fscanf(file, "cpu ");
        for(auto& i: data)
            fscanf(file, "%llu", &i);
        return data;
    }

    float API::Stats::get_ram_usage(){
        FILE* file = fopen("/proc/meminfo", "r");
        fscanf(file, "MemTotal:\t%llu kB\nMemFree:\t%llu kB\nMemAvailable:\t%llu", &ram_total, &ram_free, &ram_available);
        printf("MemTotal:\t%llu\nMemFree:\t%llu\nMemAvailable:\t%llu\n", ram_total, ram_free, ram_available);
        float result;
        if(!fclose(file)){
            result = (long double)(ram_total - ram_available) / (long double)ram_total * (long double)100;
        }else{
            result = -1;
        }
        return result;
    }
    float API::Stats::get_cpu_usage(){
        std::vector<unsigned long long> cpu_data = std::move(get_cpu_data());
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
        std::vector<unsigned long long> new_cpu_data = std::move(get_cpu_data());
        unsigned long long total_time = 0, idle_time = 0;
        float result = 0;

        for(std::size_t i = 0; i < 10; i++){
            total_time += new_cpu_data[i] - cpu_data[i];
        }
        for(std::size_t i = 3; i < 5; i++){
            idle_time += new_cpu_data[i] - cpu_data[i];
        }
        result = (long double)(total_time - idle_time) / (long double)(total_time) * (long double)100;
        cpu_data = std::move(new_cpu_data);
        return result;
    }
    float API::Stats::get_disk_usage(){
        float result;
        if (!statvfs("/", &buffer)) {
            result = ((long double)(buffer.f_blocks - buffer.f_bfree) / (long double)buffer.f_blocks) * (long double)100;
        }else{
            result = -1;
        }
        return result;
    }

    API::RCON::RCON(){
        /*
        std::cout << "Test\n";
        long long i = 0;
        std::cout << "Test0\n";
        client = std::move(std::make_unique<srcon>("127.0.0.1", 25575, "1337228"));
        std::cout << "Test1\n";
        while(!client->is_connected() && i < 100){
            std::cout << "Connection failed, trying again...\n";
            std::cout << "Test0\n";
            client = std::move(std::make_unique<srcon>("127.0.0.1", 25575, "1337228"));
            i++;
            std::cout << "Test1\n";
        }
        std::cout << "Test2\n";
        if(!client->is_connected()){
            std::cout << "RCON initialization failed. RCON API won't work.\n";
        }else{
            std::cout << "Connected successfully!\n";
            client->send("say It's WORKING!");
            std::cout << client->send("say hello") << " <- response on \"" << "say hello" << "\"\n";
        }
        std::cout << "Test3\n";
        */
    }

    char const* API::RCON::exec_command(std::string cmd){
        return "1234";
    }
    /*char const* API::RCON::get_history(int count, int offset){
        return "1234";
    }*/
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
