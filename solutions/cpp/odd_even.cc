// Copyright (c) 2015 Elements of Programming Interviews. All rights reserved.

#include <functional>
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using std::ref;
using std::cout;
using std::endl;
using std::thread;
using std::mutex;
using std::lock_guard;
using std::unique_lock;
using std::condition_variable;

// @include
class OddEvenMonitor {
 public:
  static const bool ODD_TURN = true;
  static const bool EVEN_TURN = false;

  OddEvenMonitor() : turn_(ODD_TURN) {}

  void wait_turn(bool old_turn) {
    unique_lock<mutex> lock(mx_);
    while (turn_ != old_turn) {
      cond_.wait(lock);
    }
  }

  void toggle_turn() {
    lock_guard<mutex> lock(mx_);
    turn_ = !turn_;
    cond_.notify_one();
  }

 private:
  bool turn_;
  condition_variable cond_;
  mutex mx_;
};

void odd_thread(OddEvenMonitor& monitor) {
  for (int i = 1; i <= 100; i+= 2) {
    monitor.wait_turn(OddEvenMonitor::ODD_TURN);
    cout << i << endl;
    monitor.toggle_turn();
  }
}

void even_thread(OddEvenMonitor& monitor) {
  for (int i = 2; i <= 100; i+= 2) {
    monitor.wait_turn(OddEvenMonitor::EVEN_TURN);
    cout << i << endl;
    monitor.toggle_turn();
  }
}
// @exclude

int main(int argc, char* argv[]) {
  OddEvenMonitor monitor;
  thread t1(odd_thread, ref(monitor));
  thread t2(even_thread, ref(monitor));
  t1.join();
  t2.join();
  return 0;
}
