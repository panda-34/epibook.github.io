// Copyright (c) 2015 Elements of Programming Interviews. All rights reserved.

#include <string>
#include <vector>
#include <iostream>
#include <iomanip>
#include <chrono>
#include <thread>
#include <mutex>

using std::string;
using std::to_string;
using std::vector;
using std::cout;
using std::endl;
using std::setprecision;
using std::chrono::system_clock;
using std::chrono::milliseconds;
using std::chrono::duration;
using std::chrono::duration_cast;
using std::thread;
using std::this_thread::sleep_for;
using std::mutex;
using std::lock_guard;
using std::unique_lock;

class ServiceRequest {
 public:
  ServiceRequest(const string& s) : request_(s) {}

  string extract_word_to_check_from_request() {
    return request_;
  }

 private:
  string request_;
};

class ServiceResponse {
 public:
  const vector<string>& response() {
    return response_;
  }

  void encode_into_response(const vector<string>& s) {
    response_ = s;
  }

 private:
  vector<string> response_;
};

vector<string> closest_in_dictionary(const string& w) {
  sleep_for(milliseconds(200));
  return {w + "_result"};
}

// @include
class SpellCheckService {
 public:
  static void service(ServiceRequest& req, ServiceResponse& resp) {
    string w = req.extract_word_to_check_from_request();
    vector<string> result;
    bool found = false;
    {
      lock_guard<mutex> lock(mx);
      if (w == w_last) {
        result = closest_to_last_word;
        found = true;
      }
    }
    if (!found) {
      result = closest_in_dictionary(w);
      lock_guard<mutex> lock(mx);
      w_last = w;
      closest_to_last_word = result;
    }
    resp.encode_into_response(result);
  }

 private:
  static string w_last;
  static vector<string> closest_to_last_word;
  static mutex mx;
};
// @exclude
string SpellCheckService::w_last;
vector<string> SpellCheckService::closest_to_last_word;
mutex SpellCheckService::mx;

void service_thread(const string& data) {
  auto start_time = system_clock::now();
  ServiceRequest req(data);
  ServiceResponse resp;
  SpellCheckService::service(req, resp);
  duration<float> running_time = system_clock::now() - start_time;
  cout << data << " -> " << resp.response()[0] << " (" << setprecision(3) <<
    running_time.count() << " sec)" << endl;
}

int main(int argc, char* argv[]) {
  int i = 0;
  while (true) {
    thread(service_thread, "req:" + to_string(i+1)).detach();
    if (i > 0) {
      // while req:i+1 is computed we could return req:i from the cache
      thread(service_thread, "req:" + to_string(i)).detach();
    }
    sleep_for(milliseconds(500));
    ++i;
  }
}