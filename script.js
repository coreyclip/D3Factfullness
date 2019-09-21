const url = 'data/json/Indicator_HDI.json';

d3.json(url)
    .then(res => {
    console.dir(res);
    alert('check console')
}).catch((err) => {
        console.log(err);
      alert("Oh no, something horrible happened!")
  })