vector<string> extract_steps(string& data)
{
    size_t max_steps = 1000;
    vector<string> recipe_data = match_regex(data, RECIPE_REGEX, max_steps);
    vector<string> sentences;
    for (string& str : recipe_data)
    {
        str.erase(0, 33);
        str.erase(str.end() - 4, str.end());
        size_t begin_sent = 0;
        size_t len = str.length();
        while (begin_sent < len)
        {
            size_t end_sent = str.find(".", begin_sent);
            if (end_sent == string::npos)
            {
                sentences.push_back(str.substr(begin_sent));
                begin_sent = end_sent;
            }
            else 
            {
                sentences.push_back(str.substr(begin_sent, end_sent - begin_sent + 1));
                begin_sent = end_sent + 1;
            }
        }
    }
    return sentences;
}
