#include <boost/python.hpp>
#include "api.h"

BOOST_PYTHON_MODULE(api_cpp)
{
    using namespace boost::python;
    def("greet", AJ::API::greet);
    class_<AJ::API::Stats>("stats")
        .def("get_ram_usage", &AJ::API::Stats::get_ram_usage)
        .def("get_cpu_usage", &AJ::API::Stats::get_cpu_usage)
        .def("get_disk_usage", &AJ::API::Stats::get_disk_usage)
        ;
    class_<AJ::API::RCON>("rcon")
        .def("exec_command", &AJ::API::RCON::exec_command)
        //.def("get_history", &AJ::API::RCON::get_history)
        ;
    class_<AJ::API::BackupManagement>("backup")
        .def("make", &AJ::API::BackupManagement::make)
        .def("info", &AJ::API::BackupManagement::info)
        .def("list", &AJ::API::BackupManagement::list)
        .def("switch_to", &AJ::API::BackupManagement::switch_to)
        ;
}
