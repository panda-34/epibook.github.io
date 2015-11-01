// Copyright (c) 2015 Elements of Programming Interviews. All rights reserved.

#include <string>
#include <functional>
#include <iostream>
#include <boost/chrono.hpp>
#include <boost/thread/scoped_thread.hpp>

using std::string;
using std::bind;
using std::cout;
using std::endl;
using boost::chrono::milliseconds;
using boost::scoped_thread;
using boost::this_thread::sleep_for;
using boost::thread_interrupted;

const milliseconds TIMEOUT(500);

// @include
class Requestor {
// @exclude
 public:
  Requestor(const string& request, int delay) : req_(request), delay_(delay) {}

  string finished() {
    return "response:" + req_;
  }

  string error() {
    return "response:" + req_ + ":TIMEDOUT";
  }

// @include
  string execute() {
    try {
      // simulate the time taken to perform a computation
      sleep_for(delay_);
    }
    catch (const thread_interrupted&) {
      return error();
    }
    return finished();
  }
// @exclude

  void process_response(const string& response) {
    cout << "ProcessResponse:" << response << endl;
  }

// @include
  void actual_task() {
    string response = execute();
    process_response(response);
  }

  void task() {
    scoped_thread<> inner_thread(&Requestor::actual_task, this);
    if (!inner_thread.try_join_for(TIMEOUT)) {
      inner_thread.interrupt();
    }
  }

  void dispatch() {
    thread_ = scoped_thread<>(&Requestor::task, this);
  }

// @exclude
 private:
  string req_;
  milliseconds delay_;
  scoped_thread<> thread_;
// @include
};
// @exclude

int main(int argc, char* argv[]) {
  Requestor r1("t1", 1000); r1.dispatch();
  Requestor r2("t2", 100); r2.dispatch();
  Requestor r3("t3", 10); r3.dispatch();
  Requestor r4("t4", 1); r4.dispatch();
  Requestor r5("t5", 2); r5.dispatch();
  return 0;
}
