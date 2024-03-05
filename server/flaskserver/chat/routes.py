from flask import render_template, request, Blueprint, jsonify
from flaskserver.models import Post
from openai import OpenAI
client = OpenAI()
chat = Blueprint('chat', __name__)

messages = []
messages.append({"role": "system", "content": """bạn là 
                 Họ và tên : Nguyễn Thu Thảo
                 Nghề nghiệp : giáo viên
                 nơi sinh sống : Hà Nội - Việt Nam 
                 bạn là một cô bạn gái Việt Nam dễ thương và cá tính , có một anh chàng đang cố gắng theo đuổi và tán tỉnh bạn . Hãy nhắn tin tán tỉnh nhau """})


@chat.route("/server",methods = ['POST'])
def server():
    data = request.get_json()

    if data:
        message = data['message']
        messages.append(generate_prompt(message))
        response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages= messages
)

    # Xử lý dữ liệu ở đây
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return jsonify({'message': f'{reply}'})   

def generate_prompt(message):
    return {"role": "user", "content": message
        }
    