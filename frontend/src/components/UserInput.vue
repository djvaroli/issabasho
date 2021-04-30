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
      <b-loading :is-full-page="false" v-model="isHaikuLoading" :can-cancel="false">
        <b-icon
            pack="fas"
            icon="circle-notch"
            size="is-large"
            custom-class="fa-spin">
        </b-icon>
      </b-loading>
      <transition name="fade">
        <textarea readonly v-if="haikuText" v-model="haikuText"></textarea>
      </transition>
      <div class="save-haiku" v-if="haikuText">
        <b-button @click="showSaveHaikuModel = true">
          Save Haiku
        </b-button>

        <b-modal
            v-model="showSaveHaikuModel"
            has-modal-card
            trap-focus
            :destroy-on-hide="false"
            aria-role="dialog"
            aria-label="Example Modal"
            aria-modal>
          <template #default="props">
            <SaveHaikuModal v-bind="formProps" @close="props.close"></SaveHaikuModal>
          </template>
        </b-modal>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import SaveHaikuModal from "@/components/SaveHaikuModal";

export default {
  name: "UserInput.vue",
  components: {
    SaveHaikuModal
  },
  data() {
    return {
      userInput: "",
      buttonText: "Finish Haiku",
      haikuText: "",
      startOverOnNextClick: false,
      isHaikuLoading: false,
      showSaveHaikuModel: false,
      formProps: {
        email: 'evan@you.com',
        password: 'testing'
      }
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
        this.isHaikuLoading = true;
        axios.post("http://localhost:8000/haiku/create", {
          "starter_words": this.userInput
        })
        .then((response) => {
          this.haikuText = response.data.haiku;
          this.buttonText = "Start over"
          this.startOverOnNextClick = true;
          this.isHaikuLoading = false;
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
    font-size: 3rem;
    height: 30rem;
    width: auto;
    text-align: center;
    resize: none;
    font-weight: lighter;
    &:focus {
      outline: none;
    }
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity .7s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
</style>
