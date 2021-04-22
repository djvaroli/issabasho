<template>
    <b-navbar class="custom-navbar" spaced="True">
        <template #brand>
          <b-navbar-item tag="router-link" :to="{ path: '/' }" class="custom-navbar-item">
            <img
                src="https://storage.googleapis.com/issa-public/issa-o-logo-k-small.png"
            >
          </b-navbar-item>
        </template>
        <template #end>
        </template>
    </b-navbar>
</template>

<script>
export default {
  name: "Navbar.vue"
}
</script>

<style scoped lang="scss">
.custom-navbar {
   background: $empty-space-color;
   color: $empty-space-color;
   //border-bottom: 3px solid $primary-color;
   //box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
   .custom-navbar-item {
     color: $primary-color;
     font-size: 2rem;
     font-weight: bold;
     transition: 0.25s;
     padding-bottom: 1.5rem;
     border-bottom: 5px solid $primary-color;
     &:hover {
       background-color: $empty-space-color;
       color: $accent-color;
       transition: 0.25s;
     }
   }
 }
</style>
