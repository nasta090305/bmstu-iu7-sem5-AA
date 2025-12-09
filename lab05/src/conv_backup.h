#pragma once
#include<queue>
#include<mutex>
#include "sqlite3.h"
#include"task.hpp"
#define LOG_FILE "log.txt"
/*
*      Q1         Q2        Q3          Q4
* Gen ----> Read ----> Ext ----> Write ----> Log
*/
using conv_belt = queue<shared_ptr<Task>>;
class Generator
{
public:
	Generator() = default;
	~Generator() = default;

	void Gen_tasks(size_t tasks_num, conv_belt& queue);
};

class Reader
{
public:
	Reader() = default;
	~Reader() = default;

	void Read_tasks(size_t tasks_num, conv_belt& in_queue, conv_belt& out_queue);
private:
	void read_recipe(shared_ptr<Task> task);
};

class Extractor
{
public:
	Extractor() = default;
	~Extractor() = default;

	void Extract_tasks(size_t tasks_num, conv_belt& in_queue, conv_belt& out_queue);
private:
	void extract_recipe(shared_ptr<Task> task);
};

class Writer
{
public:
	Writer() = default;
	~Writer() = default;

	int init_db();
	void Write_tasks(size_t tasks_num, conv_belt& in_queue, conv_belt& out_queue);
private:
	sqlite3* DB;
	void write_task(shared_ptr<Task> task);
};

struct total_time
{
	double time_on_gen = 0.0;
	double time_on_read = 0.0;
	double time_on_extr = 0.0;
	double time_on_write = 0.0;
	double time_on_destr = 0.0;
	double time_await_q1 = 0.0;
	double time_await_q2 = 0.0;
	double time_await_q3 = 0.0;
	double time_await_q4 = 0.0;
	double time_existence = 0.0;
};

class Logger
{
public:
	total_time totals;
	Logger() = default;
	~Logger() = default;

	void Log_tasks(size_t tasks_num, conv_belt& in_queue);
private:
	void log_task(shared_ptr<Task> task);
	void adjust_totals(shared_ptr<Task> task);
	double tp_diff(chrono::high_resolution_clock::time_point fir, chrono::high_resolution_clock::time_point sec);

	ofstream log_file = ofstream(LOG_FILE);
	vector<pair<chrono::time_point<chrono::high_resolution_clock>, string>> time_points;
};


bool compare(const pair<chrono::time_point<chrono::high_resolution_clock>, string>& fir, const pair<chrono::time_point<chrono::high_resolution_clock>, string>& sec);