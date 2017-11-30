// Generated by CoffeeScript 2.0.2
(function() {
  var Queue, QueueError, Set, dicts;

  dicts = require("./dicts");

  Set = class Set {
    constructor(...markings) {
      var i, len, m;
      this.d = new dicts.Dict();
      for (i = 0, len = markings.length; i < len; i++) {
        m = markings[i];
        this.add(m);
      }
    }

    empty() {
      return this.d.empty();
    }

    len() {
      return this.d.len();
    }

    add(marking) {
      return this.d.set(marking, null);
    }

    get(marking) {
      return this.d.getitem(marking)[0];
    }

    has(marking) {
      return this.d.has(marking);
    }

    * iter() {
      var _, m, ref, results, x;
      ref = this.d.iter();
      results = [];
      for (x of ref) {
        [m, _] = x;
        results.push((yield m));
      }
      return results;
    }

  };

  QueueError = class QueueError {
    constructor(message) {
      this.message = message;
      this.name = "QueueError";
    }

  };

  Queue = class Queue {
    constructor(...markings) {
      var i, len, m;
      this.data = {};
      this.head = 0;
      this.tail = 0;
      for (i = 0, len = markings.length; i < len; i++) {
        m = markings[i];
        this.put(m);
      }
    }

    empty() {
      return this.head === this.tail;
    }

    full() {
      return this.head === this.tail + 1;
    }

    put(marking) {
      if (this.full()) {
        throw new QueueError("cannot put on full queue");
      }
      this.data[this.tail] = marking;
      return this.tail++;
    }

    get() {
      var m;
      if (this.empty()) {
        throw new QueueError("cannot get from empty queue");
      }
      m = this.data[this.head];
      delete this.data[this.head];
      this.head++;
      return m;
    }

  };

  module.exports = {
    Set: Set,
    QueueError: QueueError,
    Queue: Queue
  };

}).call(this);

//# sourceMappingURL=sets.js.map