from nxtools import NxConanFile
from conans import tools


class CrowConan(NxConanFile):
    name = "crow"
    version = "49edf898"
    license = "BSD"
    url = "https://github.com/hoxnox/conan-crow"
    license = "https://github.com/ipkn/crow/blob/49edf898a5b9a39a0d69072cc2434c4f23692908/LICENSE"
    settings = "os", "compiler", "build_type", "arch"
    build_policy = "missing"
    description = "Crow is C++ microframework for web. (inspired by Python Flask)"
    requires = ("boost/1.66.0@hoxnox/stable")
    options = {}

    def do_source(self):
        self.retrieve("8863e630403669f9cc4598a3368f50053a98354ad2b85075384df99628b598f0",
                [
                    "vendor://ipkn/crow/crow-{v}.zip".format(v=self.version),
                    "https://codeload.github.com/ipkn/crow/zip/49edf898a5b9a39a0d69072cc2434c4f23692908"
                ],
                "crow-{v}.zip".format(v=self.version))

    def do_build(self):
        tools.unzip("crow-{v}.zip".format(v=self.version), "{staging_dir}/src".format(staging_dir=self.staging_dir))

    def do_package(self):
        self.copy(pattern="*", dst="include", src="{staging_dir}/src/crow-49edf898a5b9a39a0d69072cc2434c4f23692908/include".format(staging_dir=self.staging_dir))
