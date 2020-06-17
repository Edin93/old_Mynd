<template>
  <div class="main">
    <sui-grid centered :columns="3">
      <sui-grid-column v-if="post">
        <!-- <sui-segment> -->
          <sui-image class="pimg" :src="'http://localhost:1337' + post.image.url" fluid />
        <sui-comment-group>
          <h3 is="sui-header" dividing>Comments</h3>

          <sui-comment>
            <sui-comment-avatar
              src="https://semantic-ui-vue.github.io/static/images/avatar/small/matt.jpg"
            />
            <sui-comment-content>
              <a is="sui-comment-author">Matt</a>
              <sui-comment-metadata>
                <div>Today at 5:42PM</div>
              </sui-comment-metadata>
              <sui-comment-text>How artistic!</sui-comment-text>
              <sui-comment-actions>
                <sui-comment-action>Reply</sui-comment-action>
              </sui-comment-actions>
            </sui-comment-content>
          </sui-comment>

          <sui-comment>
            <sui-comment-avatar
              src="https://semantic-ui-vue.github.io/static/images/avatar/small/matt.jpg"
            />
            <sui-comment-content>
              <a is="sui-comment-author">Elliot Fu</a>
              <sui-comment-metadata>
                <div>Yesterday at 12:30AM</div>
              </sui-comment-metadata>
              <sui-comment-text>
                <p>
                  This has been very useful for my research. Thanks as well!
                </p>
              </sui-comment-text>
              <sui-comment-actions>
                <sui-comment-action>Reply</sui-comment-action>
              </sui-comment-actions>
            </sui-comment-content>
          </sui-comment>
          <sui-comment>
            <sui-comment-avatar
              src="https://semantic-ui-vue.github.io/static/images/avatar/small/matt.jpg"
            />
            <sui-comment-content>
              <a is="sui-comment-author">Joe Henderson</a>
              <sui-comment-metadata>
                <div>5 days ago</div>
              </sui-comment-metadata>
              <sui-comment-text>
                Dude, this is awesome. Thanks so much
              </sui-comment-text>
              <sui-comment-actions>
                <sui-comment-action>Reply</sui-comment-action>
              </sui-comment-actions>
            </sui-comment-content>
          </sui-comment>

          <sui-form reply>
            <textarea rows="2" class="pri"></textarea>

            <sui-button
              content="Add Reply"
              label-position="left"
              icon="edit"
              primary
              class="pri"
            />
          </sui-form>
        </sui-comment-group>

        <sui-rail position="right">
          <sui-segment>
            <div>
              <sui-image
                :src="
                  'http://localhost:1337' +
                    post.user.profile_img.formats.thumbnail.url
                "
                avatar
              />
              <span>{{ post.user.username }}</span>
            </div>
            <div text-align="left" class="details">
              <b>Description</b>
              <p>
                {{ post.description }}
              </p>
            </div>
            <div class="tags">
              <!-- <a v-for="topic in post.topics"  is="sui-label" tag>
                {{ topic.title }}
              </a> -->
            </div>
            <div class="likes">
              <sui-icon slot="trigger" name="heart" color="red" size="large" />
              2k
            </div>
          </sui-segment>
        </sui-rail>
        <!-- </sui-segment> -->
      </sui-grid-column>
    </sui-grid>
  </div>
</template>

<script>
import gql from "graphql-tag";
export default {
  components: {},
  apollo: {
    post: gql`
      query getPost {
        post(id: 1) {
          description
          id
          image {
            url
          }
          user {
            username
            id
            profile_img {
              formats
            }
          }
          topics {
            id
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

.pri {
  margin-top: 1em;
}
.details {
  margin: 1.5em 0;
}
.tag {
  margin: 5px;
}
.likes {
  margin-top: 1em;
}
.pimg {
  border-radius: .28571429rem;
box-shadow: 0 1px 3px 0 #d4d4d5,0 0 0 1px #d4d4d5;
}
</style>
