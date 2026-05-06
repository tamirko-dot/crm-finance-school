from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from documents.models import LearningDocument, DocumentAccessLog, DocumentTag


@login_required
def document_list(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q", "").strip()
    file_type = request.GET.get("type", "")
    tag_slug = request.GET.get("tag", "")

    qs = LearningDocument.objects.filter(is_active=True).select_related("domain").prefetch_related("tags")

    if query:
        qs = qs.filter(title_he__icontains=query) | LearningDocument.objects.filter(
            description_he__icontains=query, is_active=True
        )
        qs = qs.distinct()

    if file_type:
        qs = qs.filter(file_type=file_type)

    if tag_slug:
        qs = qs.filter(tags__slug=tag_slug)

    tags = DocumentTag.objects.all().order_by("name_he")
    file_types = LearningDocument.objects.filter(is_active=True).values_list("file_type", flat=True).distinct()

    return render(request, "documents/document_list.html", {
        "documents": qs.order_by("-created_at"),
        "query": query,
        "file_type": file_type,
        "tag_slug": tag_slug,
        "tags": tags,
        "file_types": sorted(set(file_types)),
    })


@login_required
def document_download(request: HttpRequest, pk: int) -> HttpResponse:
    doc = get_object_or_404(LearningDocument, pk=pk, is_active=True)
    DocumentAccessLog.objects.create(user=request.user, document=doc)
    return redirect(doc.file_url)
