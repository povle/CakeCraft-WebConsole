#include <string>

namespace AJ{
    class API{
    public:
        static char const* greet();
        class Stats{
        public:
            float get_ram_usage();
            float get_cpu_usage();
            float get_disk_usage();
        };
        class RCON{
        public:
            char const* exec_command(std::string cmd);
            char const* get_history(int count, int offset);
        };
        class BackupManagement{
        public:
            char const* make(std::string name, std::string desc);
            char const* info(int type, std::string name_or_timestamp);
            char const* list(int count, int type_from, std::string from, int type_to, std::string to);
            char const* switch_to(int type, std::string name_or_timestamp);
        };
    };
}
