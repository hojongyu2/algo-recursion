var rc = require(".././recursionChallenge");

describe("flatten", function() {
  it("flatten should take in a multi-demensional array and return a one-dimensional array", function() {
    expect(rc.flatten([[1,2],[3,4]])).toEqual([1,2,3,4]);
  });
});

// use the specs from the previous exercises to test the rest of the methods.
