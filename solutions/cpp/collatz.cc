// Copyright (c) 2015 Elements of Programming Interviews. All rights reserved.

#include <cassert>
#include <string>
#include <functional>
#include <utility>
#include <unordered_set>
#include <iostream>
#include <chrono>
#include <boost/thread.hpp>
#include <boost/thread/sync_bounded_queue.hpp>

using std::stoi;
using std::bind;
using std::ref;
using std::pair;
using std::make_pair;
using std::unordered_set;
using std::cout;
using std::endl;
using std::chrono::system_clock;
using std::chrono::milliseconds;
using std::chrono::duration_cast;
using boost::thread_group;
using boost::sync_bounded_queue;
using boost::queue_op_status;

typedef unsigned long long collatz_int;
typedef sync_bounded_queue<pair<collatz_int, collatz_int>> queue_type;
void worker(collatz_int lower, collatz_int upper);
bool collatz_check(collatz_int x, unordered_set<collatz_int>& visited);

// @include
void thread_func(queue_type& q) {
  pair<collatz_int, collatz_int> args;
  while (q.wait_pull_front(args) == queue_op_status::success) {
    worker(args.first, args.second);
  }
}

// Performs basic unit of work
void worker(collatz_int lower, collatz_int upper) {
  for (collatz_int i = lower; i <= upper; ++i) {
    assert(collatz_check(i, unordered_set<collatz_int>()));
  }
  cout << '(' << lower << ',' << upper << ')' << endl;
}

// Checks an individual number
bool collatz_check(collatz_int x, unordered_set<collatz_int>& visited) {
  if (x == 1) {
    return true;
  }
  if (!visited.emplace(x).second) {
    return false;
  }
  if (x & 1) {  // odd number
    return collatz_check(3 * x + 1, visited);
  } else {  // even number
    return collatz_check(x >> 1, visited);  // divide by 2
  }
}
// @exclude

int main(int argc, char* argv[]) {
  collatz_int N = 10000000;
  collatz_int RANGESIZE = 1000000;
  int NTHREADS = 4;
  if (argc > 1) {
    N = stoi(argv[1]);
  }
  if (argc > 2) {
    RANGESIZE = stoi(argv[2]);
  }
  if (argc > 3) {
    NTHREADS = stoi(argv[3]);
  }

  assert(collatz_check(1, unordered_set<collatz_int>()));
  assert(collatz_check(3, unordered_set<collatz_int>()));
  assert(collatz_check(8, unordered_set<collatz_int>()));
  auto start_time = system_clock::now();

// @include
  // Uses synchronized bounded queue for task assignment and load balancing
  queue_type q(NTHREADS);
  thread_group threads;
  for (int i = 0; i < NTHREADS; ++i) {
    threads.create_thread(bind(thread_func, ref(q)));
  }
  for (collatz_int i = 0; i < N / RANGESIZE; ++i) {
    q << make_pair(i * RANGESIZE + 1, (i + 1) * RANGESIZE);
  }
  q.close();
  threads.join_all();

// @exclude
  cout << "Finished all threads" << endl;
  auto running_time = duration_cast<milliseconds>(system_clock::now() - start_time).count();
  cout << "time in milliseconds for checking to " << N << " is " <<
    running_time << '(' << N/running_time << " per ms)";

  return 0;
}