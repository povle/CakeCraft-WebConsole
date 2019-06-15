#include <boost/python.hpp>
#include "api.h"

BOOST_PYTHON_MODULE(api_backend)
{
    using namespace boost::python;
    def("greet", greet);
}
