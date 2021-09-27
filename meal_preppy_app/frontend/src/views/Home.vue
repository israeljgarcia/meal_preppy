<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Courses/>
  </div>
</template>

<script>
// @ is an alias to /src
import Courses from '@/components/Courses.vue';

export default {
  name: 'Course',
  components: {
    Courses,
  },
};
</script>
