"use strict";

const restartButtons = document.querySelectorAll(".restart-button");
restartButtons.forEach((button) => button.addEventListener("click", newGame));

function newGame() {
  console.log("newGame called");
  fetch("/new_game")
    .then((response) => response.json())
    .then((data) => {
      updateGrid(data.board);
      document.querySelector(".game-message").classList.remove("game-over");
    })
    .catch((error) => console.error("Error:", error));
}

function updateGrid(board) {
  console.log("updateGrid called");
  const cells = document.querySelectorAll("td");
  board.flat().forEach((value, index) => {
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
      updateGrid(data.board);
      if (data.game_over) {
        document.querySelector(".game-message").classList.add("game-over");
      }
    })
    .catch((error) => console.error("Error:", error));
}

document.addEventListener("keydown", (event) => {
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
});
