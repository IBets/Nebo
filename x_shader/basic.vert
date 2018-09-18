#version 310 es

#define VERT_POSITION   0
#define VERT_COLOR      1
#define VERT_SIZE       2



layout (location = VERT_POSITION)   in vec3  a_VertexPosition;
layout (location = VERT_COLOR)      in vec3  a_VertexColor;
layout (location = VERT_SIZE)       in float a_VertexSize;


uniform mat4 u_MVP;

out vec3 a_Color;


void main()
{
   	
    gl_Position = u_MVP * vec4(a_VertexPosition, 1.0);
    gl_PointSize = a_VertexSize;
    a_Color = a_VertexColor;
   
}
