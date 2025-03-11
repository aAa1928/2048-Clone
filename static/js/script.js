"use strict";

const restartButtons = document.querySelectorAll(".restart-button");
restartButtons.forEach((button) => button.addEventListener("click", newGame));

const gameOverMessage = document.getElementById("game-over-message");
const gameOverOverlay = document.querySelector(".game-over-overlay");
const winOverlay = document.querySelector(".win-overlay");
let gameOver = null;
let score = null;
let bestScore = null;

function newGame() {
  console.log("newGame called");
  fetch("/new_game")
    .then((response) => response.json())
    .then((data) => {
      updateGrid(data.grid);
      updateScore(0);
      gameOverOverlay.hidden = true;
      winOverlay.hidden = true;
      gameOverOverlay.style.animation = "";
      winOverlay.style.animation = "";
      gameOver = false;
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

function updateScore(newScore) {
  console.log("updateScore called");
  score = newScore;
  document.getElementById("score").textContent = score;
  document.getElementById("final-score").textContent = score;
}

function updateBestScore(newBestScore) {
  console.log("updateBestScore called");
  bestScore = newBestScore;
  document.getElementById("best-score").textContent = bestScore;
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
      updateScore(data.score);
      updateBestScore(data.best_score);
      document.getElementById("score").textContent = score;
      console.log("win:", data.won);
      if (data.is_won) {
        console.log("You won!");
        displayWinMessage();
      }
      if (data.game_over) {
        displayGameOverMessage();
      }
    })
    .catch((error) => console.error("Error:", error));
}

function displayGameOverMessage() {
  console.log("displayGameOverMessage called");
  gameOver = true;
  gameOverOverlay.hidden = false;
  gameOverOverlay.style.animation = "fadeIn 0.5s ease-in forwards";
}

function displayWinMessage() {
  console.log("displayWinMessage called");
  winOverlay.hidden = false;
  winOverlay.style.animation = "fadeIn 0.5s ease-in forwards";

  const keepGoingButton = document.querySelector(".keep-going-button");
  keepGoingButton.addEventListener("click", () => {
    winOverlay.hidden = true;
    winOverlay.style.animation = "";
  });
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
