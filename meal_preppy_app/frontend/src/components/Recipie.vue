<template>
    <div class="card">
      <div class="card-image">
        <figure class="image is-4by3">
          <img :src="recipie.image" alt="Placeholder image" />
        </figure>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <p class="title is-4">{{ recipie.title }}</p>
          </div>
        </div>

        <div class="content">
          <p v-html="recipie.summary"></p>
          <br />
          <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
        </div>
      </div>
    </div>
</template>
<script>
export default {
  name: 'Recipie',
  props: ['recipie'],
};
</script>
<style scoped>
p {
  max-height: 200px;
  overflow: scroll;
}

img {
  width: 200px;
}
</style>
