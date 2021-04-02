import SearchForm from "./SearchForm"

function App() {
  return (
    <div className="App">
      <SearchForm />
      <textarea data-test-id="output-text" id="output-text"></textarea>
    </div>
  );
}

export default App;
