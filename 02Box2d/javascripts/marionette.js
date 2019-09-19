$(function() {
  
  var controller = new Leap.Controller();
  
  var   b2Vec2 = Box2D.Common.Math.b2Vec2
        ,	b2BodyDef = Box2D.Dynamics.b2BodyDef
        ,	b2Body = Box2D.Dynamics.b2Body
        ,	b2FixtureDef = Box2D.Dynamics.b2FixtureDef
        ,	b2Fixture = Box2D.Dynamics.b2Fixture
        ,	b2World = Box2D.Dynamics.b2World
        ,	b2MassData = Box2D.Collision.Shapes.b2MassData
        ,	b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape
        ,	b2CircleShape = Box2D.Collision.Shapes.b2CircleShape
        , b2DistanceJointDef = Box2D.Dynamics.Joints.b2DistanceJointDef
      
        ,	b2DebugDraw = Box2D.Dynamics.b2DebugDraw;
     
    // 构造一个世界对象
    world = new b2World(
         new b2Vec2(0, 10)    //gravity        世界重力向量
      ,  true                 //allow sleep    物体是否可休眠。通过不模拟休眠物体来提高引擎的效率。
    );

    var fixDef = new b2FixtureDef;
    fixDef.density = 1.0;
    fixDef.friction = 0.5;
    fixDef.restitution = 0.2;
    
    var bodyDef = new b2BodyDef;
    //create ground
    bodyDef.type = b2Body.b2_staticBody;
    bodyDef.position.x = 20;
    bodyDef.position.y = 30;
    fixDef.shape = new b2PolygonShape;
    fixDef.shape.SetAsBox(10, 0.5);
    world.CreateBody(bodyDef).CreateFixture(fixDef);
    
    
    bodyDef.type = b2Body.b2_dynamicBody;
    
    fixDef.shape = new b2CircleShape(2);
    
    bodyDef.position.x = 12;
    bodyDef.position.y = 20;
    
    var playerA = world.CreateBody(bodyDef);
    playerA.CreateFixture(fixDef);
    
    bodyDef.position.x = 20;
    
    var playerB = world.CreateBody(bodyDef)
    playerB.CreateFixture(fixDef);
    
    fixDef.shape = new b2CircleShape(1);
    bodyDef.position.x = 12;
    bodyDef.position.y = 10;
   
    var holderA = world.CreateBody(bodyDef)
    holderA.CreateFixture(fixDef);
    
    bodyDef.position.x = 19;
    var holderB = world.CreateBody(bodyDef);
    holderB.CreateFixture(fixDef);
   
    var jointDef = new b2DistanceJointDef();
    
    jointDef.bodyA = playerA;
    jointDef.bodyB = holderA;
    
    var zerovec = new b2Vec2(0, 0);
    
    jointDef.localAnchorA = zerovec;
    jointDef.localAnchorB = zerovec;
    
    jointDef.length = 10;
    jointDef.dampingRatio = 0.8;
    jointDef.frequencyHz = 20;
    
    world.CreateJoint(jointDef);
    
    jointDef.bodyA = playerB;
    jointDef.bodyB = holderB;
    
    world.CreateJoint(jointDef);
    
    
    
    
    var debugDraw = new b2DebugDraw();
    debugDraw.SetSprite(document.getElementById("stage").getContext("2d"));
    debugDraw.SetDrawScale(20.0);
    debugDraw.SetFillAlpha(0.3);
    debugDraw.SetLineThickness(1.0);
    debugDraw.SetFlags(b2DebugDraw.e_shapeBit | b2DebugDraw.e_jointBit);
    world.SetDebugDraw(debugDraw);
    
    controller.on('animationFrame', function(frame) {
      var i;
      if (frame.hands.length >= 1) {        
        var hand = frame.hands[0];
        var y = hand.palmPosition[1];
        
        if(hand.fingers.length >= 2) {
          var holders = [holderA, holderB, holderC, holderD, holderE];
          
          var sorted = hand.fingers.sort(function(a,b) {
            return a.stabilizedTipPosition[0] - b.stabilizedTipPosition[0];
          })
          
          for(i=0,l=5;i<l;i++) {
            var finger = sorted[i];
            var x = finger.stabilizedTipPosition[0];
            var y = finger.stabilizedTipPosition[1];
            holders[i].SetPosition(new b2Vec2((x+400)/20, (600-y) / 20));
          }
        }
      }
      world.Step(
            1 / 60   //frame-rate
         ,  10       //velocity iterations
         ,  10       //position iterations
      );
      world.DrawDebugData();
      world.ClearForces();
    });
    
    controller.connect();
    
  
});