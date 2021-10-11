<template>
  <div class="userhome">
    <div class="home-container columns is-multiline is-centered">
      <div class="column is-10 is-10-mobile">
        <h1 class="is-size-3 has-text-centered has-text-weight-bold">Home</h1>
        <hr class="heading-line " />
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <h2 class="is-size-4">Welcome {{ userData.firstName }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      userData: {},
    };
  },
  methods: {
    getUserData() {
      const path = 'http://localhost:5000/users/home';
      axios
        .get(path, {
          withCredentials: true,
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
          },
        })
        .then((res) => {
          this.userData = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getUserData();
  },
};
</script>
<style scoped>
.heading-line {
  background: black;
  border-radius: 15px;
  height: 1.5px;
}
</style>
