// Below is an example of Jasmine. Use the specs and the example below to test your code.
const rc = require(".././recursionChallenge");

describe("toRoman", function() {
  it("toRoamn should take in an arabic number a return a string with its roman numeral counterpart", function() {
    expect(rc.romanNum(toRoman(12))).toEqual('XII');
  });
});
