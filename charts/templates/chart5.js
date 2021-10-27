const data = [];
const data2 = [];
let prev = 100;
let prev2 = 80;
for (let i = 0; i < 1000; i++) {
  prev += 5 - Math.random() * 10;
  data.push({x: i, y: prev});
  prev2 += 5 - Math.random() * 10;
  data2.push({x: i, y: prev2});
}
const totalDuration = 10000;
const delayBetweenPoints = totalDuration/data.length;
const previousY = (ctx) => ctx.index === 0 ? ctx.chart.scales.y.getPixelForValue(
  100) :ctx.chart.getDatasetMeta(ctx.datasetIndex).data[ctx.index - 1].getProps([
  'y'], true).y;
var ctx = document.getElementById(id).getContext('2d');
var myChart = new Chart(ctx, {
type : 'line',
data : {
  datasets: [{
    borderColor: 'red',
    borderWidth: 1,
    redius : 0,
    data : data,
    },
    {
    borderColor: 'blue',
    borderWidth: 1,
    redius : 0,
    data : data2,
    }
  ]
},
options : {
  animation : {
    x : {
      type : 'number',
      easing : 'linear',
      duration : delayBetweenPoints,
      from : NaN,
      delay(ctx){
        if (ctx.type !== 'data' || ctx.xStarted){
          return 0;
        }
        ctx.xStarted = true;
        return ctx.index * delayBetweenPoints;
      }
    },
    y : {
      type : 'number',
      easing : 'linear',
      duration : delayBetweenPoints,
      from : previousY,
      delay(ctx){
        if (ctx.type !== 'data' || ctx.xStarted){
          return 0;
        }
        ctx.xStarted = true;
        return ctx.index * delayBetweenPoints;
      }
    }
  },
  interaction : {
    intersect : false
  },
  plugins : {
    legend : false
  },
  scales : {
    x : {
      type : 'linear'
    }
  }
}

});