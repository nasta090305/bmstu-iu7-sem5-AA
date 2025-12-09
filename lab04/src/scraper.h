#pragma once
#define CURL_STATICLIB
#include<string>
#include<fstream>
#include<iostream>
#include<regex>
#include <curl\curl.h>

#define EXIT_LIB 2
#define START_URL "https://volshebnaya-eda.ru/category/kollekcia-receptov/"
#define LINK_REGEX "\"https://volshebnaya-eda.ru/\\S+\""
#define RECIPE_TAG u8"recipe-procedure-text"
#define RECIPE_REGEX "<p class=\"recipe-procedure-text\">[^a-zA-Z<>]+</p>"
#define KOSTYL 100

using namespace std;

size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp);

string link_valid(string);

vector<string> match_regex(string input, string expression, size_t& nmax);

vector<string> scrape_recipe_links(string& buffer, size_t& nmax);

int load_page(string& buffer, string url);

template <typename T>
int scrape_records(size_t nmax, vector<T>& records, string start_url, size_t& start_page, vector<T>(*scraper) (T&, size_t&), int (*loader)(T&, string))
{
    while (nmax)
    {
        string tmp = "page/" + to_string(start_page++) + "/";
        string url = start_url + tmp;
        T buffer;
        int res = loader(buffer, url);
        if (res != EXIT_SUCCESS)
            return res;
        vector<T> out_vec = scraper(buffer, nmax);
        records.insert(records.end(), out_vec.begin(), out_vec.end());
    }
    return EXIT_SUCCESS;
}

int get_recipe(string url, string& recipe);

void extract_recipe(string url, string filename);

void g_recipe(string url);
