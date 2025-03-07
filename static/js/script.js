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
