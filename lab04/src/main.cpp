#define _CRT_SECURE_NO_WARNINGS 
#include<iostream>
#include<thread>
#include<stdio.h>
#include<chrono>
#include<format>
#include"scraper.h"
#define RECIPES 500

void menu()
{
    cout << "Menu: " << endl;
    cout << "0. Exit." << endl;
    cout << "1. Regular download." << endl;
    cout << "2. Multithreaded download." << endl;
    cout << "3. Bench." << endl;
    cout << "Select an option: ";
}

int main()
{
    setlocale(LC_ALL, "Russian");
    int option = 1;
    while (option)
    {
        menu();
        cin >> option;
        if (option == 0)
            return EXIT_SUCCESS;
        else if (option == 1)
        {
            vector<string> recipes_urls;
            size_t page_cnt = 0;
            cout << "Enter a number of recipes to download: ";
            size_t max_recipes;
            cin >> max_recipes;
            int res = scrape_records(max_recipes, recipes_urls, START_URL, page_cnt, scrape_recipe_links, load_page);
            if (res == EXIT_FAILURE)
            {
                cout << "Unable to perform" << endl;
                return EXIT_FAILURE;
            }
            else if (res == EXIT_LIB)
            {
                cout << "Unable to load library" << endl;
                return EXIT_LIB;
            }
            //последовательное скачивание
            size_t cnt = 1;
            string tmp = "./out/", tmp2 = ".txt";
            for (auto& recipe : recipes_urls)
            {
                string out;
                if (get_recipe(recipe, out) != EXIT_SUCCESS)
                {
                    cout << "Unable to load recipe" << endl;
                    return EXIT_FAILURE;
                }
                string f = tmp + to_string(cnt) + tmp2;
                cout << f << endl;
                ofstream fout(f);
                fout << out;
                fout.close();
                cout << "Recipe " << to_string(cnt++) << " was downloaded" << endl;
            }
        }
        else if (option == 2)
        {
            vector<string> recipes_urls;
            size_t page_cnt = 1;
            cout << "Enter a number of recipes to download: ";
            size_t max_recipes;
            cin >> max_recipes;
            int res = scrape_records(max_recipes, recipes_urls, START_URL, page_cnt, scrape_recipe_links, load_page);
            if (res == EXIT_FAILURE)
            {
                cout << "Unable to perform" << endl;
                return EXIT_FAILURE;
            }
            else if (res == EXIT_LIB)
            {
                cout << "Unable to load library" << endl;
                return EXIT_LIB;
            }
            //параллельное скачивание
            cout << "Enter a number of additional threads: ";
            size_t max_threads;
            cin >> max_threads;
            vector<thread> thds(max_threads);
            size_t thread_cnt, recipe_cnt;
            curl_global_init(CURL_GLOBAL_ALL);
            for (recipe_cnt = 0; recipe_cnt < max_recipes;)
            {
                for (thread_cnt = 0; (thread_cnt < max_threads) && (recipe_cnt < max_recipes); thread_cnt++, recipe_cnt++)
                {
                    string filename = "out/" + to_string(recipe_cnt + 1) + ".txt";
                    thds[thread_cnt] = thread(extract_recipe, recipes_urls[recipe_cnt], filename);
                }
                max_threads = thread_cnt;
                for (thread_cnt = 0; thread_cnt < max_threads; thread_cnt++)
                {
                    thds[thread_cnt].join();
                    cout << "Thread " << thread_cnt + 1 << " was terminated" << endl;
                }
            }
            curl_global_cleanup();
        }
        else if (option == 3)
        {
            vector<size_t> threads_cnt = { 1, 2, 4, 8, 16, 32};
            vector<string> recipes_urls;
            size_t page_cnt = 1;
            int res = scrape_records(RECIPES, recipes_urls, START_URL, page_cnt, scrape_recipe_links, load_page);
            if (res == EXIT_FAILURE)
            {
                cout << "Unable to perform" << endl;
                return EXIT_FAILURE;
            }
            else if (res == EXIT_LIB)
            {
                cout << "Unable to load library" << endl;
                return EXIT_LIB;
            }
            // cout << "done extracting urls";
            FILE* f = fopen("out/out.csv", "w");
            if (f == NULL)
                return EXIT_FAILURE;
            fprintf(f, "threads_cnt,avg_t\n");
            for (size_t amount : threads_cnt)
            {
                chrono::duration<double, std::milli> sum(0.0);
                vector<thread> thds(amount);
                size_t thread_cnt, recipe_cnt;
                auto beg = chrono::high_resolution_clock::now();
                curl_global_init(CURL_GLOBAL_ALL);
                size_t max_limit = amount;
                for (recipe_cnt = 0; recipe_cnt < RECIPES;)
                {
                    for (thread_cnt = 0; (thread_cnt < max_limit) && (recipe_cnt < RECIPES); thread_cnt++, recipe_cnt++)
                    {
                        string filename;
                        thds[thread_cnt] = thread(g_recipe, recipes_urls[recipe_cnt]);
                    }
                    max_limit = thread_cnt;
                    for (thread_cnt = 0; thread_cnt < max_limit; thread_cnt++)
                    {
                        thds[thread_cnt].join();
                        //cout << "Thread " << thread_cnt + 1 << " was termiinated" << endl;
                    }
                }
                curl_global_cleanup();
                sum += chrono::high_resolution_clock::now() - beg;
                //cout << "threads_cnt: " << amount << " avg_time: " << sum.count() << endl;
                fprintf(f, "%zu,%lf\n", amount, sum.count());
                printf("%zu,%lf\n", amount, sum.count());

            }
            fclose(f);
        }
        else
            cout << "Invalid option." << endl;
    }
}