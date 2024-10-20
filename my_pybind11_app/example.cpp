#include <pybind11/pybind11.h>

namespace py = pybind11;

double add(double a, double b) {
    return a + b;
}

double multiply(double a, double b) {
    return a * b;
}

PYBIND11_MODULE(example, m) {
    m.def("add", &add, "A function that adds two numbers");
    m.def("multiply", &multiply, "A function that multiplies two numbers");
}
