require_relative 'recursion_challenge'

# Use the specs from the previous exercises to test. This time, however, write
# your tests using rspec.
describe "Recursion Challenge" do
  it "flatten should take in a multi-demensional array and return a one-dimensional array" do
    expect(flatten([[1,2],[3,4]])).to eq([1,2,3,4])
  end
end
