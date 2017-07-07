#include <crow.h>

int
main(int argc, char* argv[])
{
	crow::SimpleApp app;
	CROW_ROUTE(app, "/")([](const crow::request& req)
		{ return crow::response("Hello, world"); });
	return 0;
}

