<template>
  <div class="main">
    <sui-grid centered :columns="2">
      <sui-grid-column>
        <sui-card-group :items-per-row="3" stackable>
          <sui-card v-for="post in posts" :key="post.id">
            <sui-image  :src="'http://localhost:1337' + post.image.url" />
            <!-- <div v-if="post.image.height < 700" class="po">
              <sui-image
                src="https://semantic-ui-vue.github.io/static/images/avatar/small/matt.jpg"
                avatar size="small"
              />
              <span>Username</span>

            </div>
            <div>
              <p v-if="post.image.height < 600" class="desc" >{{ post.description}}</p>
            </div> -->
          </sui-card>
        </sui-card-group>
      </sui-grid-column>
    </sui-grid>
  </div>
</template>

<script>
import gql from "graphql-tag";
export default {
  components: {},
  apollo: {
    posts: gql`
      query getPosts {
        posts {
          id
          description
          image {
            url
            width
            height
            formats
          }
        }
      }
    `
  }
};
</script>

<style scoped>
.main {
  margin-top: 7em;
}
.details {
  margin-top: 1em;
}
.unbox {
  box-shadow: 0 0 0 0 #ffffff, 0 0 0 0 #d4d4d5;
}
.po {
  margin: 1.5em 1.5em 0.8em;
}
.desc {
  margin-left: 1.5em;
}
.card {
  box-shadow: none;
}
</style>
