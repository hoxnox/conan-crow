from nxtools import NxConanFile
from conans import tools


class CrowConan(NxConanFile):
    name = "crow"
    version = "4e39b23e"
    license = "BSD"
    url = "https://github.com/hoxnox/conan-crow"
    license = "https://raw.githubusercontent.com/ipkn/crow/4e39b23e455e455f1878b3e68d729a1737f3e431/LICENSE"
    settings = "os", "compiler", "build_type", "arch"
    build_policy = "missing"
    description = "Crow is C++ microframework for web. (inspired by Python Flask)"
    requires = ("boost/1.66.0@hoxnox/stable")
    options = {}

    def do_source(self):
        self.retrieve("417064e3a2238c3877877e5ed9902686c87596440d426b893027abd7a5b5a52d",
                [
                    "vendor://ipkn/crow/crow-{v}.zip".format(v=self.version),
                    "https://github.com/ipkn/crow/archive/4e39b23e455e455f1878b3e68d729a1737f3e431.zip"
                ],
                "crow-{v}.zip".format(v=self.version))

    def do_build(self):
        tools.unzip("crow-{v}.zip".format(v=self.version), "{staging_dir}/src".format(staging_dir=self.staging_dir))

    def do_package(self):
        self.copy(pattern="*", dst="include", src="{staging_dir}/src/crow-4e39b23e455e455f1878b3e68d729a1737f3e431/include".format(staging_dir=self.staging_dir))
