import graphene

from graphene_django import DjangoObjectType, DjangoListField 
from .models import Book 
from .models import Comment
from .models import Idea
from .models import User 


class BookType(DjangoObjectType): 
    class Meta:
        model = Book
        fields = "__all__"

class UserType(DjangoObjectType): 
    class Meta:
        model = User
        fields = "__all__"

class IdeaType(DjangoObjectType): 
    class Meta:
        model = Idea
        fields = "__all__"

class CommentType(DjangoObjectType): 
    class Meta:
        model = Comment
        fields = "__all__"

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, book_id=graphene.Int())

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_book(self, info, book_id):
        return Book.objects.get(pk=book_id)

    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, user_id=graphene.Int())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, user_id):
        return User.objects.get(pk=user_id)

    all_ideas = graphene.List(IdeaType)
    idea = graphene.Field(IdeaType, idea_id=graphene.Int())

    def resolve_all_ideas(self, info, **kwargs):
        return Idea.objects.all()

    def resolve_idea(self, info, idea_id):
        return Idea.objects.get(pk=idea_id)

    comment_by_idea = graphene.List(CommentType, idea_id=graphene.Int())

    def resolve_comment_by_idea(self, info, idea_id):
        try:
            return Comment.objects.filter(idea_id=idea_id)
        except Comment.DoesNotExist:
            return None

class CommentInput(graphene.InputObjectType):
    id = graphene.ID()
    comment = graphene.String()
    description = graphene.String()
    eventName = graphene.String()
    idea_id = graphene.Int() 
    user_id = graphene.Int() 

class CreateComment(graphene.Mutation):
    class Arguments:
        comment_data = CommentInput(required=True)

    comment = graphene.Field(CommentType)

    @staticmethod
    def mutate(root, info, comment_data=None):
        comment_instance = Comment( 
            comment=comment_data.comment,
            description=comment_data.description,
            eventName=comment_data.eventName,
            idea_id=comment_data.idea_id,
            user_id=comment_data.user_id
        )
        comment_instance.save()
        return CreateComment(comment=comment_instance)

class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()

class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required=True)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, user_data=None):
        user_instance = User( 
            name=user_data.name,
            email=user_data.email
        )
        user_instance.save()
        return CreateUser(user=user_instance)

class IdeaInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    eventName = graphene.String()
    user_id = graphene.Int()

class CreateIdea(graphene.Mutation):
    class Arguments:
        idea_data = IdeaInput(required=True)

    idea = graphene.Field(IdeaType)

    @staticmethod
    def mutate(root, info, idea_data=None):
        idea_instance = Idea( 
            title=idea_data.title,
            description=idea_data.description,
            eventName=idea_data.eventName,
            user_id=idea_data.user_id
        )
        idea_instance.save()
        return CreateIdea(idea=idea_instance)

class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    year_published = graphene.String()
    review = graphene.Int() 

class CreateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):
        book_instance = Book( 
            title=book_data.title,
            author=book_data.author,
            year_published=book_data.year_published,
            review=book_data.review
        )
        book_instance.save()
        return CreateBook(book=book_instance)

class UpdateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):

        book_instance = Book.objects.get(pk=book_data.id)

        if book_instance:
            book_instance.title = book_data.title
            book_instance.author = book_data.author
            book_instance.year_published = book_data.year_published
            book_instance.review = book_data.review
            book_instance.save()

            return UpdateBook(book=book_instance)
        return UpdateBook(book=None)

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id):
        book_instance = Book.objects.get(pk=id)
        book_instance.delete()

        return None

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    create_comment = CreateComment.Field()
    create_user = CreateUser.Field()
    create_idea = CreateIdea.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)