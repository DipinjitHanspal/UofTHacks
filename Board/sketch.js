var button, lg;
var grid = [];

function setup () {
  scale(5)
  var cnv = createCanvas(660, 820)
  cnv.position((windowWidth - width) / 2, (windowHeight - height)/2)
  background(48)
}

function draw () {
  scale(5)  // Scales all objects by 5
  stroke(1.4, 55)
  for (var l = 0; l < 15; l++) {
    grid[l]=[];  // 2-D array for the button objects
    for (var i = 0; i < 15; i ++){
      grid [l][i] = new Square()
      grid[l][i].move((i + 0.25) * 8.5, (l + 0.2) * 10.5);
      grid[l][i].display();
    }
  }
  var letter = new Tile()
  letter.display('ABXDEAFH')
}

function update() {
  for (var l = 0; l < 15; l++) {
    for (var i = 0; i < 15; i ++){
      grid [l][i].mousePressed()
    }
  }
}

function Square() {
  this.x = 0
  this.y = 5
  this.move = function (x, y) {
    this.x = x
    this.y = y
  }
  this.display = function () {
    rect(this.x, this.y, 8, 10).fill(255, 235, 215)
  }
  this.mousePressed = function (lg) {
    this.x = mouse.x
    this.y = mouse.y
  }
};

function Tile() {
  this.letter = function () {
    var x = 'A'
  }
  this.display = function (letter) {
    var tile = new Square ()
    rect(2, 2, 8, 10)
    var t_let = text(letter, 3, 12)
    t_let.textSize( 3)
  }
};
