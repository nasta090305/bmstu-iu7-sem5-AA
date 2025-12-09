#include"scraper.h"
#include<iostream>
using namespace std;

size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp)
{
    ((string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

string link_valid(string input)
{
    input.erase(0, 1); 
    input.pop_back(); 
    //cout << input << endl;
    string buffer;
    load_page(buffer, input);
    if (buffer.find(RECIPE_TAG) == string::npos)
        return "";
    return input;
}

vector<string> match_regex(string input, string expression, size_t& nmax)
{
    regex reg(expression);
    auto beg = sregex_iterator(input.begin(), input.end(), reg);
    auto end = sregex_iterator();

    vector<string> words;

    while ((beg != end))
    {
        words.push_back(beg->str());
        ++beg;
    }

    return words;
}

vector<string> scrape_recipe_links(string& buffer, size_t& nmax)
{

    vector<std::string> links = match_regex(buffer, LINK_REGEX, nmax);
    vector<std::string> recipe_links;
    for (auto& link : links)
    {
        std::string recipe_link = link_valid(link);
        if (recipe_link.size() > 0 && nmax)
        {
            recipe_links.push_back(recipe_link);
            nmax--;
        }
    }
    return recipe_links;
}

int load_page(string& buffer, string url)
{
    CURL* curl = curl_easy_init();
    if (curl == NULL)
        return EXIT_LIB;
    curl_easy_setopt(curl, CURLOPT_USERAGENT, "google");
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &buffer);

    CURLcode res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    if (res != CURLE_OK)
        return EXIT_FAILURE;

    return EXIT_SUCCESS;
}

int get_recipe(string url, string& recipe)
{
    string buffer;
    int res = load_page(buffer, url);
    if (res != EXIT_SUCCESS)
        return res;
    size_t kostyl = 1000;
    vector<string> out = match_regex(buffer, RECIPE_REGEX, kostyl);
    for (auto& part : out)
    {

        part.erase(0, 33);
        part.erase(part.end() - 4, part.end());
        recipe.append(part + " ");
    }
    return EXIT_SUCCESS;
}


void extract_recipe(string url, string filename)
{
    string out;
    if (get_recipe(url, out) != EXIT_SUCCESS)
    {
        cout << "Unable to load recipe" << endl;
        return;
    }
    ofstream fout(filename);
    fout << out;
    fout.close();
}

void g_recipe(string url)
{
    string buffer;
    string b;
    int res = load_page(buffer, url);
    if (res != EXIT_SUCCESS)
        return;
    size_t kostyl = 1000;
    vector<string> out = match_regex(buffer, RECIPE_REGEX, kostyl);
    for (auto& part : out)
    {

        part.erase(0, 33);
        part.erase(part.end() - 4, part.end());
        //cout << part << endl;
        b.append(part + " ");
    }
}