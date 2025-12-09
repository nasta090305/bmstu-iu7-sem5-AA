//#include"Conveyor.hpp"
//#include<iostream>
//#include<algorithm>
//
//mutex q1_mtx, q2_mtx, q3_mtx, q4_mtx;
//
//void Generator::Gen_tasks(size_t tasks_num, conv_belt& queue)
//{
//    size_t page_cnt = 0;
//    vector<string> urls_buffer;
//    int res = scrape_records(tasks_num, urls_buffer, START_URL, page_cnt, scrape_recipe_links, load_page);
//    if (res == EXIT_FAILURE)
//    {
//        cout << "Unable to perform" << endl;
//        return;
//    }
//    else if (res == EXIT_LIB)
//    {
//        cout << "Unable to load library" << endl;
//        return;
//    }
//    shared_ptr<Task> tp;
//    size_t id = 1;
//    for (string& url : urls_buffer)
//    {
//        tp = make_shared<Task>(Task());
//        tp->time_points.start_gen = chrono::high_resolution_clock::now();
//        tp->set_id(id++);
//        tp->set_url(url);
//        //unique_lock автоматически вызывает mutex.unlock() при выходе из области видимости
//        {
//            unique_lock<mutex> lock(q1_mtx);
//            queue.push(tp);
//            tp->time_points.pushed_q1 = chrono::high_resolution_clock::now();
//        }
//        //cout << "Task: " << tp->get_id() <<  " url: " << tp->get_url() << " entered Q1" << endl;
//    }
//    cout << "All tasks generated" << endl;
//}
//
//void Reader::read_recipe(shared_ptr<Task> task)
//{
//    string buffer;
//    int res = load_page(buffer, task->get_url());
//    if (res != EXIT_SUCCESS)
//    {
//        cout << "Unable to load page" << endl;
//        return;
//    }
//    //cout << buffer;
//    task->set_raw_data(buffer);
//}
//
//void Reader::Read_tasks(size_t tasks_num, conv_belt& in_queue, conv_belt& out_queue)
//{
//    size_t cnt = 0;
//
//    while (cnt < tasks_num)
//    {
//        if (in_queue.empty())
//            continue;
//        shared_ptr<Task> tp;
//        {
//            unique_lock<mutex> lock(q1_mtx);
//            tp = in_queue.front();
//            tp->time_points.start_read = chrono::high_resolution_clock::now();
//            in_queue.pop();
//            //cout << "Task: " << tp->get_id() << " url: " << tp->get_url() << " quit Q1" << endl;
//        }
//        this->read_recipe(tp);
//        {
//            unique_lock<mutex> lock(q2_mtx);
//            out_queue.push(tp);
//            tp->time_points.pushed_q2 = chrono::high_resolution_clock::now();
//            //cout << "Task: " << tp->get_id() << " url: " << tp->get_url() << " raw_data_sample: " << tp->get_raw_data().substr(0, 10) << " entered Q2" << endl;
//        }
//        cnt++;
//    }
//    cout << "All tasks read" << endl;
//}
//
//
//void Extractor::Extract_tasks(size_t tasks_num, conv_belt& in_queue, conv_belt& out_queue)
//{
//    size_t cnt = 0;
//
//    while (cnt < tasks_num)
//    {
//        if (in_queue.empty())
//            continue;
//        shared_ptr<Task> tp;
//        {
//            unique_lock<mutex> lock(q2_mtx);
//            tp = in_queue.front();
//            tp->time_points.start_extr = chrono::high_resolution_clock::now();
//            in_queue.pop();
//            //cout << "Task: " << tp->get_id() << " url: " << tp->get_url() << " quit Q1" << endl;
//        }
//        this->extract_recipe(tp);
//        {
//            unique_lock<mutex> lock(q3_mtx);
//            out_queue.push(tp);
//            tp->time_points.pushed_q3 = chrono::high_resolution_clock::now();
//            //cout << "Task: " << tp->get_id() << " url: " << tp->get_url() << " raw_data_sample: " << tp->get_raw_data().substr(0, 10) << " entered Q2" << endl;
//        }
//        cnt++;
//    }
//    cout << "All tasks extracted" << endl;
//}
//
//void Extractor::extract_recipe(shared_ptr<Task> task)
//{
//    string raw_data = task->get_raw_data();
//    string img_url = extract_img_url(raw_data);
//    string title = extract_title(raw_data);
//    vector<string> steps = extract_steps(raw_data);
//    vector<vector<string>> ingridients = extract_ingridients(raw_data);
//    task->set_title(title);
//    task->set_image_url(img_url);
//    task->set_steps(steps);
//    task->set_ingridients(ingridients);
//    task->clear_raw_data();
//}
//
//void Writer::Write_tasks(size_t tasks_num, conv_belt& in_queue, conv_belt& out_queue)
//{
//    if (this->init_db() == EXIT_FAILURE)
//        return;
//    size_t cnt = 0;
//
//    while (cnt < tasks_num)
//    {
//        if (in_queue.empty())
//            continue;
//        shared_ptr<Task> tp;
//        {
//            unique_lock<mutex> lock(q3_mtx);
//            tp = in_queue.front();
//            tp->time_points.start_write = chrono::high_resolution_clock::now();
//            in_queue.pop();
//            //cout << "Task: " << tp->get_id() << " url: " << tp->get_url() << " quit Q1" << endl;
//        }
//        this->write_task(tp);
//        {
//            unique_lock<mutex> lock(q4_mtx);
//            out_queue.push(tp);
//            tp->time_points.pushed_q4 = chrono::high_resolution_clock::now();
//            //cout << "Task: " << tp->get_id() << " url: " << tp->get_url() << " raw_data_sample: " << tp->get_raw_data().substr(0, 10) << " entered Q2" << endl;
//        }
//        cnt++;
//    }
//    sqlite3_close(this->DB);
//    cout << "All tasks written" << endl;
//}
//
//int Writer::init_db()
//{
//    int rc = sqlite3_open("recipes.db", &this->DB);
//    if (rc != SQLITE_OK) {
//        cout << "Can't open database" << endl;
//        return EXIT_FAILURE;
//    }
//    char* message_error;
//    string creation = "CREATE TABLE IF NOT EXISTS RECIPES("
//        "ID INT PRIMARY KEY NOT NULL, "
//        "ISSUE_ID INT NOT NULL, "
//        "URL TEXT NOT NULL, "
//        "TITLE TEXT NOT NULL, "
//        "INGREDIENTS TEXT NOT NULL, "
//        "STEPS TEXT NOT NULL, "
//        "IMAGE_URL TEXT NOT NULL );";
//    rc = sqlite3_exec(this->DB, creation.c_str(), nullptr, nullptr, &message_error);
//    if (rc != SQLITE_OK) {
//        cout << "Can't create table" << endl;
//        sqlite3_free(message_error);
//        return EXIT_FAILURE;
//    }
//    creation = "DELETE FROM RECIPES;";
//    rc = sqlite3_exec(this->DB, creation.c_str(), nullptr, nullptr, &message_error);
//    if (rc != SQLITE_OK) {
//        cout << "Can't truncate table" << endl;
//        sqlite3_free(message_error);
//        return EXIT_FAILURE;
//    }
//    cout << "DB init success" << endl;
//    return EXIT_SUCCESS;
//}
//
//void Writer::write_task(shared_ptr<Task> task)
//{
//    string ingr = "[", stps = "[";
//    vector<vector<string>> tmp_i = task->get_ingridients();
//    vector<string> tmp_s = task->get_steps();
//
//    for (string& el : tmp_s)
//        stps += "\"" + el + "\", ";
//    stps.erase(stps.end() - 2);
//    stps += "]";
//
//    for (auto& el : tmp_i)
//        ingr += "{\"name\": \"" + el[0] + "\", \"unit\": \"" + el[2] + "\", \"quantity\": \"" + el[1] + "\"}" + ", ";
//    ingr.erase(ingr.end() - 2);
//    ingr += "]";
//
//    string sql = "INSERT INTO RECIPES VALUES(" + to_string(task->get_id()) + ", " + to_string(task->get_issue_id()) +
//        ", " + "'" + task->get_url() + "'" + ", " + "'" + task->get_title() + "'" +
//        ", " + "'" + ingr + "'" + ", " + "'" + stps + "'" +
//        ", " + "'" + task->get_image_url() + "');";
//
//    char* message_error;
//    int rc = sqlite3_exec(this->DB, sql.c_str(), nullptr, nullptr, &message_error);
//    if (rc != SQLITE_OK) {
//        cout << "SQL error: " << message_error << endl;
//        cout << "Conflicting SQL query: " << sql << endl;
//        sqlite3_free(message_error);
//        return;
//    }
//}
//
//
//void Logger::Log_tasks(size_t tasks_num, conv_belt& in_queue)
//{
//    size_t cnt = 0;
//
//    while (cnt < tasks_num)
//    {
//        if (in_queue.empty())
//            continue;
//        shared_ptr<Task> tp;
//        {
//
//            unique_lock<mutex> lock(q4_mtx);
//            tp = in_queue.front();
//            tp->time_points.start_destr = chrono::high_resolution_clock::now();
//            in_queue.pop();
//        }
//        cnt++;
//        tp->time_points.end_destr = chrono::high_resolution_clock::now();
//        this->log_task(tp);
//        this->adjust_totals(tp);
//    }
//    cout << "All tasks read" << endl;
//
//    sort(this->time_points.begin(), this->time_points.end(), compare);
//    for (const auto& el : this->time_points)
//        this->log_file << el.first.time_since_epoch().count() << " " << el.second << endl;
//
//    cout << "Average existence time: " << this->totals.time_existence / tasks_num << " s." << std::endl;
//
//    cout << "Average generation time: " << this->totals.time_on_gen / tasks_num << " s." << std::endl;
//    cout << "Average reading time: " << this->totals.time_on_read / tasks_num << " s." << std::endl;
//    cout << "Average data extraction time: " << this->totals.time_on_extr / tasks_num << " s." << std::endl;
//    cout << "Average data base writing time: " << this->totals.time_on_write / tasks_num << " s." << std::endl;
//    cout << "Average logging and destruction time: " << this->totals.time_on_destr / tasks_num << " s." << std::endl;
//
//    cout << "Average waiting in queue1 time: " << this->totals.time_await_q1 / tasks_num << " s." << std::endl;
//    cout << "Average waiting in queue2 time: " << this->totals.time_await_q2 / tasks_num << " s." << std::endl;
//    cout << "Average waiting in queue3 time: " << this->totals.time_await_q3 / tasks_num << " s." << std::endl;
//    cout << "Average waiting in queue4 time: " << this->totals.time_await_q4 / tasks_num << " s." << std::endl;
//    this->log_file.close();
//}
//
//void Logger::log_task(shared_ptr<Task> task)
//{
//    size_t id = task->get_id();
//    this->time_points.emplace_back(task->time_points.start_gen, " ID #" + to_string(id) + " started generation process");
//    this->time_points.emplace_back(task->time_points.pushed_q1, " ID #" + to_string(id) + " pushed in queue1");
//    this->time_points.emplace_back(task->time_points.start_read, " ID #" + to_string(id) + " started reading process");
//    this->time_points.emplace_back(task->time_points.pushed_q2, " ID #" + to_string(id) + " pushed in queue2");
//    this->time_points.emplace_back(task->time_points.start_extr, " ID #" + to_string(id) + " started extraction process");
//    this->time_points.emplace_back(task->time_points.pushed_q3, " ID #" + to_string(id) + " pushed in queue3");
//    this->time_points.emplace_back(task->time_points.start_write, " ID #" + to_string(id) + " started writing to DB process");
//    this->time_points.emplace_back(task->time_points.pushed_q4, " ID #" + to_string(id) + " pushed in queue4");
//    this->time_points.emplace_back(task->time_points.start_destr, " ID #" + to_string(id) + " started destruction process");
//    this->time_points.emplace_back(task->time_points.end_destr, " ID #" + to_string(id) + " ended destruction process");
//}
//
//
//void Logger::adjust_totals(shared_ptr<Task> task)
//{
//    this->totals.time_on_gen += tp_diff(task->time_points.start_gen, task->time_points.pushed_q1);
//    this->totals.time_on_read += tp_diff(task->time_points.start_read, task->time_points.pushed_q2);
//    this->totals.time_on_extr += tp_diff(task->time_points.start_extr, task->time_points.pushed_q3);
//    this->totals.time_on_write += tp_diff(task->time_points.start_write, task->time_points.pushed_q4);
//    this->totals.time_on_destr += tp_diff(task->time_points.start_destr, task->time_points.end_destr);
//    this->totals.time_await_q1 += tp_diff(task->time_points.pushed_q1, task->time_points.start_read);
//    this->totals.time_await_q2 += tp_diff(task->time_points.pushed_q2, task->time_points.start_extr);
//    this->totals.time_await_q3 += tp_diff(task->time_points.pushed_q3, task->time_points.start_write);
//    this->totals.time_await_q4 += tp_diff(task->time_points.pushed_q4, task->time_points.start_destr);
//    this->totals.time_existence += tp_diff(task->time_points.start_gen, chrono::high_resolution_clock::now());
//
//}
//double Logger::tp_diff(chrono::high_resolution_clock::time_point fir, chrono::high_resolution_clock::time_point sec)
//{
//    chrono::duration<double> diff = sec - fir;
//    return diff.count();
//}
//
//bool compare(const pair<chrono::time_point<chrono::high_resolution_clock>, string>& fir, const pair<chrono::time_point<chrono::high_resolution_clock>, string>& sec)
//{
//    return fir.first.time_since_epoch() < sec.first.time_since_epoch();
//}