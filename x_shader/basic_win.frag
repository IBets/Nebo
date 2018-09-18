#version 330

in  vec3  a_Color;
out vec4 FragColor;

void main() {
	float dist = distance(gl_PointCoord, vec2(0.5, 0.5));
    if(dist < 0.5){
        if(dist < 0.1)
             FragColor = vec4(a_Color.x , a_Color.y, a_Color.z , pow((1 - dist), 2));
        else
            FragColor = vec4(a_Color.x , a_Color.y, a_Color.z , pow((1 - dist), 5));
	} else {discard;}

}