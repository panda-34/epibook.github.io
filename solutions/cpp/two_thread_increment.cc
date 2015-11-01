// Copyright (c) 2015 Elements of Programming Interviews. All rights reserved.

#include <string>
#include <iostream>
#include <thread>

using std::cout;
using std::endl;
using std::stoi;
using std::thread;

// @include
static int counter = 0;

void increment_thread(int N) {
  for (int i = 0; i < N; ++i) {
    ++counter;
  }
}

void two_thread_increment_driver(int N) {
  thread T1(increment_thread, N);
  thread T2(increment_thread, N);
  T1.join();
  T2.join();

  cout << counter << endl;
}
// @exclude

int main(int argc, char* argv[]) {
  int N = argc == 2 ? stoi(argv[1]) : 1000000000;
  two_thread_increment_driver(N);
  return 0;
}
