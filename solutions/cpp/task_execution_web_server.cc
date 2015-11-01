// Copyright (c) 2015 Elements of Programming Interviews. All rights reserved.

#include <memory>
#include <functional>
#include <iostream>
#include <thread>
#include <boost/thread/sync_bounded_queue.hpp>
#include <boost/asio.hpp>

using std::shared_ptr;
using std::ref;
using std::cout;
using std::endl;
using std::thread;
using boost::system::error_code;
using boost::sync_bounded_queue;
namespace asio = boost::asio;
using asio::ip::tcp;

typedef sync_bounded_queue<shared_ptr<tcp::socket>> queue_type;

void process_req(shared_ptr<tcp::socket> sock) {
  asio::streambuf sb;
  while (true) {
    error_code e;
    size_t n = asio::read_until(*sock, sb, '\n', e);
    if (e == asio::error::eof) {
      cout << endl << "connection closed" << endl;
      break;
    }
    asio::write(*sock, sb.data());
    cout << &sb;
  }
}

// @include
void thread_func(queue_type& q) {
  while (true) {
    shared_ptr<tcp::socket> sock;
    q >> sock;
    process_req(sock);
  }
}

const unsigned short SERVERPORT = 8080;
const int NTHREADS = 2;

int main(int argc, char* argv[]) {
  queue_type q(NTHREADS);
  for (int i = 0; i < NTHREADS; ++i) {
    thread(thread_func, ref(q)).detach();
  }
  asio::io_service io_service;
  tcp::acceptor acceptor(io_service, tcp::endpoint(tcp::v4(), SERVERPORT));
  while (true) {
    shared_ptr<tcp::socket> sock(new tcp::socket(io_service));
    acceptor.accept(*sock);
    q << sock;
  }
  return 0;
}
// @exclude
