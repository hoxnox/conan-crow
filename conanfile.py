from nxtools import NxConanFile
from conans import tools


class CrowConan(NxConanFile):
    name = "crow"
    version = "0.1"
    license = "BSD"
    url = "https://github.com/hoxnox/conan-crow"
    license = "https://github.com/ipkn/crow/blob/v{v}/LICENSE".format(v=version)
    settings = "os", "compiler", "build_type", "arch"
    build_policy = "missing"
    description = "Crow is C++ microframework for web. (inspired by Python Flask)"
    requires = ("boost/1.66.0@hoxnox/stable")
    options = {}

    def do_source(self):
        self.retrieve("7cb06dea786f5e914825e8d8048e2564b5db86c8842c7fcd3beefa4cd5c4681a",
                [
                    "vendor://ipkn/crow/crow-{v}.zip".format(v=self.version),
                    "https://codeload.github.com/ipkn/crow/zip/v{v}".format(v=self.version)
                ],
                "crow-{v}.zip".format(v=self.version))

    def do_build(self):
        tools.unzip("crow-{v}.zip".format(v=self.version), "{staging_dir}/src".format(staging_dir=self.staging_dir))

    def do_package(self):
        self.copy(pattern="*", dst="include", src="{staging_dir}/src/crow-{v}/include".format(staging_dir=self.staging_dir, v=self.version))
