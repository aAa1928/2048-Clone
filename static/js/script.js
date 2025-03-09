"use strict";

const restartButtons = document.querySelectorAll(".restart-button");
restartButtons.forEach((button) => button.addEventListener("click", newGame));

let gameOver = null;

function newGame() {
  console.log("newGame called");
  fetch("/new_game")
    .then((response) => response.json())
    .then((data) => {
      updateGrid(data.grid);
      document.getElementById("game-over-message").hidden = true;
    })
    .catch((error) => console.error("Error:", error));
}

function updateGrid(grid) {
  console.log("updateGrid called");
  const cells = document.querySelectorAll("td");
  grid.flat().forEach((value, index) => {
    cells[index].textContent = value || "";
    cells[index].className = value ? `tile-${value}` : "";
  });
}

function sendMove(direction) {
  console.log(`sendMove called: ${direction}`);
  fetch(`/move/${direction}`, {
    method: "POST",
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      updateGrid(data.grid);
      if (data.game_over) {
        gameOver = false;
        document.getElementById("game-over-message").hidden = gameOver;
      }
    })
    .catch((error) => console.error("Error:", error));
}

document.addEventListener("keydown", (event) => {
  if (gameOver === null) gameOver = false;

  if (!gameOver) {
    switch (event.key) {
      case "ArrowUp":
      case "w":
      case "W":
        console.log("Up arrow pressed");
        sendMove("up");
        break;
      case "ArrowDown":
      case "s":
      case "S":
        console.log("Down arrow pressed");
        sendMove("down");
        break;
      case "ArrowLeft":
      case "a":
      case "A":
        console.log("Left arrow pressed");
        sendMove("left");
        break;
      case "ArrowRight":
      case "d":
      case "D":
        console.log("Right arrow pressed");
        sendMove("right");
        break;
    }
  }
});
