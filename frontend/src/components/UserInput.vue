<template>
  <div class="vertically-centered">
    <div class="user-input-wrapper">
      <input
          type="text"
          class="user-input"
          placeholder="Start your haiku ..."
          v-model="userInput"
      >
    </div>
    <br>
    <b-button
        id="create-haiku-button"
        @click="dispatchButtonAction"
    >
      {{ buttonText }}
    </b-button>
    <div class="generated-haiku">
      <textarea readonly v-model="haikuText"></textarea>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "UserInput.vue",
  data() {
    return {
      userInput: "",
      buttonText: "Finish Haiku",
      haikuText: "",
      startOverOnNextClick: false
    }
  },
  methods: {
    dispatchButtonAction() {
      if (this.startOverOnNextClick) {
        this.haikuText = ""
        this.buttonText = "Finish Haiku"
        this.startOverOnNextClick = false;
        this.userInput = "";
      } else {
        axios.post("http://localhost:8000/haiku/create", {
          "starter_words": this.userInput
        })
        .then((response) => {
          this.haikuText = response.data.haiku;
          this.buttonText = "Start over"
          this.startOverOnNextClick = true;
        });
      }
    }
  }
}
</script>

<style scoped lang="scss">
  .user-input {
    padding: 0.5rem;
    font-size: 3rem;
    border: 0;
    text-align: center;
    color: $accent-color;
    //border-bottom: 3px solid $primary-color;
    transition: 0.5s;
    background-color: transparent;
    font-weight: 100;
    &:focus {
        outline: none;
        //border-bottom: 1px solid $accent-color;
        transition: 0.5s;
      }
  }

  #create-haiku-button {
    border: 1px solid $primary-color;
    color: $primary-color;
    transition: 0.2s;
    &:hover {
      background-color: $primary-color;
      color: white;
      transition: 0.3s;
    }
  }

  textarea {
    margin-top: 5rem;
    color: $primary-color;
    border: none;
    padding: 1rem;
    font-size: 3.5rem;
    height: 20rem;
    width: auto;
    text-align: center;
    resize: none;
    font-weight: lighter;
    &:focus {
      outline: none;
    }
  }
</style>
