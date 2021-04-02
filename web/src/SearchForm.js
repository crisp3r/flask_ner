import axios from 'axios';
import React from 'react';

class SearchForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    const instance = axios.create({
      baseURL: 'http://localhost:5000',
      timeout: 1000,
      headers: {'X-Custom-Header': 'foobar'}
    });
    instance.post('/ner/en', {
    sentence: this.state.value
    })
    .then(function (response) {
      const data = response.data;
      const textarea = document.getElementById("output-text")
      var innerText = ""
      for (var ent of data.ents) {
        console.log(ent.ent + ":" + ent.label)
        innerText += ent.ent + ":" + ent.label + "\n";
      }
      textarea.innerHTML = innerText;
    })
    .catch(function (error) {
    console.log(error);
    });
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Enter a phrase:
          <input data-test-id="input-text" type="text" value={this.state.value} onChange={this.handleChange} />
        </label><br/>
        <input data-test-id="find-button" type="submit" value="Submit" />
      </form>
    );
  }
}


export default SearchForm;