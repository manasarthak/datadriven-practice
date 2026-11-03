With user_category_counts AS(
 select t.user_id, p.category, count(*) as purchases
 from transactions t join products p 
 on p.product_id=t.product_id
 group by t.user_id,p.category)
 
 select u1.category, u1.user_id as user1, u2.user_id as user2, 
         u1.purchases*u2.purchases as shared_categories
 from user_category_counts u1
 join user_category_counts u2
 on u1.category=u2.category
 and u1.user_id<u2.user_id
 order by u1.category,u1.user_id,u2.user_id;
